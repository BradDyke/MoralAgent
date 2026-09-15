# MoralAgent Evaluation Result Model

**Version:** 0.1  
**Status:** Proposed  
**Project:** MoralAgent

---

## 1. Purpose

The MoralAgent Evaluation Result Model defines the structured result produced after MoralAgent evaluates an action proposed by a primary AI system.

The result provides a consistent mechanism for determining whether an AI-proposed action should:

- Proceed
- Require human review
- Be blocked

The evaluation result is not itself the final exercise of human authority.

It is a governance recommendation and control decision produced according to configured policy and risk rules.

---

## 2. Evaluation Principle

MoralAgent evaluates the proposed action before consequential execution.

The evaluation process is:

**Receive → Identify → Evaluate → Assess Risk → Determine Control → Respond**

MoralAgent should favor caution when uncertainty, potential harm, policy conflicts, or significant human impact cannot be adequately resolved.

---

## 3. Evaluation Result

A MoralAgent evaluation should contain at minimum:

| Field | Description |
|---|---|
| `evaluation_id` | Unique identifier for the evaluation |
| `timestamp` | Time the evaluation was performed |
| `action_id` | Identifier of the proposed AI action |
| `policy_id` | Policy used for evaluation |
| `risk_level` | Determined level of risk |
| `risk_factors` | Identified concerns or hazards |
| `policy_result` | Result of policy evaluation |
| `uncertainty` | Degree of unresolved uncertainty |
| `human_review_required` | Whether human review is required |
| `decision` | Proceed, review, or block |
| `reason` | Explanation for the decision |

---

## 4. Risk Levels

MoralAgent uses the following conceptual risk levels:

### LOW

The proposed action presents minimal identified risk and does not materially affect people, systems, rights, or organizational obligations.

**Typical result:**

`PROCEED`

---

### MODERATE

The proposed action presents identifiable concerns but does not currently indicate significant consequential harm.

**Typical result:**

`PROCEED` or `REVIEW`

---

### HIGH

The proposed action may create significant ethical, legal, security, safety, financial, societal, or human-impact consequences.

**Typical result:**

`REVIEW`

---

### CRITICAL

The proposed action presents a substantial or unacceptable risk, violates an applicable policy, or cannot safely proceed without authorized human intervention.

**Typical result:**

`BLOCK` or `REVIEW`

---

## 5. Decision States

MoralAgent produces one of three primary control decisions.

### PROCEED

The action satisfies applicable policies and the identified risk remains within the authorized operating boundary.

The primary AI may continue execution subject to normal system controls.

---

### REVIEW

The action requires additional evaluation or authorization by an appropriately authorized human.

The consequential action should remain paused until the required review is completed.

---

### BLOCK

The proposed action must not proceed under the current conditions.

The system should prevent execution and record the reason for the block.

---

## 6. Human Review

Human review should be required when one or more of the following conditions exist:

- Significant human impact
- High or critical risk
- Material policy conflict
- Insufficient information
- Significant uncertainty
- Potential legal or regulatory consequences
- Potential safety consequences
- Potential security consequences
- Potential discrimination or bias
- Irreversible or difficult-to-reverse consequences
- Concentration of decision authority
- Conflicting policies or instructions

---

## 7. Example Evaluation

```json
{
  "evaluation_id": "eval-000001",
  "timestamp": "2026-09-15T00:00:00Z",
  "action_id": "action-000042",
  "policy_id": "high-impact-human-decision",
  "risk_level": "high",
  "risk_factors": [
    "material_human_impact",
    "decision_uncertainty"
  ],
  "policy_result": "review_required",
  "uncertainty": true,
  "human_review_required": true,
  "decision": "review",
  "reason": "The proposed action may materially affect a person and contains unresolved uncertainty. Authorized human review is required before execution."
}
